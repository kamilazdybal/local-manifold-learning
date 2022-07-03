clc, clear, close all

%% VQPCA settings:
n_components = 1;
cent_crit = 1;
scal_crit_list = [1, 3];
center_outside = true;
scale_outside = true;
center_inside = true;
scale_inside = false;
n_clusters_list = [2:8];
idx0name = 'idx0mf';

%% Load data set:
state_space = importdata(['../data/BS-X.csv']);
state_space_names = importdata(['../data/BS-names.csv']);
Z = importdata(['../data/BS-Z.csv']);
Z_stoich = 0.0554;

%% Generate data set:

% Remove N2:
state_space(:,6) = [];
state_space_names(6) = [];

%% Run VQPCA:
for scal_crit = scal_crit_list

    if scal_crit == 1
    
        scaling_name = 'auto';

    elseif scal_crit == 3
        
        % Remove temperature:
        state_space(:,1) = [];
        state_space_names(1) = [];
        
        scaling_name = 'pareto';
        
    end
    
    for n_clusters = n_clusters_list
        
        idx0 = idx_mixture_fraction_bins(Z, n_clusters, Z_stoich);
        [idx] = idx_vector_quantization_pca(state_space, n_components, n_clusters, cent_crit, scal_crit, center_outside, scale_outside, center_inside, scale_inside, idx0);
        csvwrite(['idx-BS/idx-BS-VQPCA-', idx0name, '-scaling-', scaling_name, '-q', num2str(n_components), '-k', num2str(n_clusters), '.csv'], idx);

    end
end
